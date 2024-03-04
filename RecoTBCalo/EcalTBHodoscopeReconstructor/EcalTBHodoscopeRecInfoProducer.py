import FWCore.ParameterSet.Config as cms

def EcalTBHodoscopeRecInfoProducer(**kwargs):
  mod = cms.EDProducer('EcalTBHodoscopeRecInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
