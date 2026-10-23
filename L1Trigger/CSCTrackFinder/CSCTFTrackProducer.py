import FWCore.ParameterSet.Config as cms

def CSCTFTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('CSCTFTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
