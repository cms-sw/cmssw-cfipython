import FWCore.ParameterSet.Config as cms

def TauRegionalPixelSeedTrackingRegionEDProducer(**kwargs):
  mod = cms.EDProducer('TauRegionalPixelSeedTrackingRegionEDProducer',
    RegionPSet = cms.PSet(
      ptMin = cms.double(5),
      originHalfLength = cms.double(0.2),
      originRadius = cms.double(0.2),
      deltaEtaRegion = cms.double(0.1),
      deltaPhiRegion = cms.double(0.1),
      JetSrc = cms.InputTag('icone5Tau1'),
      vertexSrc = cms.InputTag('pixelVertices'),
      searchOpt = cms.bool(False),
      howToUseMeasurementTracker = cms.string('ForSiStrips'),
      measurementTrackerName = cms.InputTag('MeasurementTrackerEvent')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
