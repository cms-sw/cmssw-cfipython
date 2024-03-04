import FWCore.ParameterSet.Config as cms

def L1GctInternJetProducer(**kwargs):
  mod = cms.EDProducer('L1GctInternJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
