import FWCore.ParameterSet.Config as cms

def RazorVarProducer(**kwargs):
  mod = cms.EDProducer('RazorVarProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
