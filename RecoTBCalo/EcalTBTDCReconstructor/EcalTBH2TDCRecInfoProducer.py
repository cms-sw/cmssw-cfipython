import FWCore.ParameterSet.Config as cms

def EcalTBH2TDCRecInfoProducer(**kwargs):
  mod = cms.EDProducer('EcalTBH2TDCRecInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
