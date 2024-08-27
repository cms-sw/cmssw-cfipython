import FWCore.ParameterSet.Config as cms

def HcalTTPDigiProducer(**kwargs):
  mod = cms.EDProducer('HcalTTPDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
