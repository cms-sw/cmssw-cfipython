import FWCore.ParameterSet.Config as cms

def ZDCDigiStudy(**kwargs):
  mod = cms.EDProducer('ZDCDigiStudy',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
