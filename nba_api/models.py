from django.db import models

# Create your models here.
class players(models.Model):
    name = models.CharField(max_length=255)
    team = models.CharField(max_length=50)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    stats = models.ManyToManyField("statistics", blank=True, related_name="stats")

    def serialize(self):
        return {
            self.name: {
                'team': self.team,
                'height': self.height,
                'weight': self.weight,
                'position': self.position,
                'stats': statistics.serialize_stats(None, self)
            }

        }
    

class statistics(models.Model):
    year = models.CharField(max_length=20)
    team = models.CharField(max_length=50)
    avg_points = models.CharField(max_length=10)
    avg_assist = models.CharField(max_length=10)
    avg_rebounds = models.CharField(max_length=10)
    avg_steals = models.CharField(max_length=10)
    avg_blocks = models.CharField(max_length=10)
    avg_turnovers = models.CharField(max_length=10)
    FG_percentage = models.CharField(max_length=10)
    TP_percantage = models.CharField(max_length=10)


    def serialize_stats(self, player):
        objects = statistics.objects.filter(player=player)
        stats = {}
        for obj in objects:
            Year = {
                obj.year:{
                    'team': obj.team,
                    'pts_per_g': obj.avg_points,
                    'ast_per_g': obj.avg_assist,
                    'reb_per_g': obj.avg_rebounds,
                    'stl_per_g': obj.avg_steals,
                    'blk_per_g': obj.avg_blocks,
                    'tov_per_g': obj.avg_turnovers,
                    'fg_pct': obj.FG_percentage,
                    'fg3_pct': obj.TP_percantage
                    }
                }
            stats.update(Year)

        return stats

