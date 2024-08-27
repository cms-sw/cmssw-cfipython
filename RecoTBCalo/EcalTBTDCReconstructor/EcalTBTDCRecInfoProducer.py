import FWCore.ParameterSet.Config as cms

def EcalTBTDCRecInfoProducer(**kwargs):
  mod = cms.EDProducer('EcalTBTDCRecInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
