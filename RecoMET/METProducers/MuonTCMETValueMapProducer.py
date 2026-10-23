import FWCore.ParameterSet.Config as cms

def MuonTCMETValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonTCMETValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
