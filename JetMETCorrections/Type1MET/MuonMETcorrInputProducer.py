import FWCore.ParameterSet.Config as cms

def MuonMETcorrInputProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
