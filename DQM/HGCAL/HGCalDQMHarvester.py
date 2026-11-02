import FWCore.ParameterSet.Config as cms

def HGCalDQMHarvester(*args, **kwargs):
  mod = cms.EDProducer('HGCalDQMHarvester',
    TemplateFiles = cms.string('Geometry/HGCalMapping/data/DQM'),
    GeometryTemplate = cms.string('geometry_v16p6.root'),
    TileboardTemplateSuffix = cms.string('_tileboard.root'),
    SkipTriggerDQM = cms.bool(True),
    SkipSlowStream = cms.bool(False),
    EnableOverflowMarkers = cms.bool(True),
    dqmQualityThreshold = cms.string('Geometry/HGCalMapping/data/DQM/dqm_quality_threshold.json'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
