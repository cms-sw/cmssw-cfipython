import FWCore.ParameterSet.Config as cms

def HLTHiggsValidator(**kwargs):
  mod = cms.EDProducer('HLTHiggsValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
