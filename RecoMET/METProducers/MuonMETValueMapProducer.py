import FWCore.ParameterSet.Config as cms

def MuonMETValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonMETValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
