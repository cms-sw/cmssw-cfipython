import FWCore.ParameterSet.Config as cms

def Run3ScoutingTrackToRecoTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('Run3ScoutingTrackToRecoTrackProducer',
    src = cms.InputTag('hltScoutingTrackPacker'),
    skipMissingProduct = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
