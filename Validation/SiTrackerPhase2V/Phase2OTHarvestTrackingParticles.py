import FWCore.ParameterSet.Config as cms

def Phase2OTHarvestTrackingParticles(**kwargs):
  mod = cms.EDProducer('Phase2OTHarvestTrackingParticles',
    TopFolderName = cms.string('TrackerPhase2OTL1TrackV'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
