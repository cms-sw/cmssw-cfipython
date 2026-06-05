import FWCore.ParameterSet.Config as cms

def Phase2OTHarvestTracks(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTHarvestTracks',
    TopFolderName = cms.string('TrackerPhase2OTL1TrackV'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
