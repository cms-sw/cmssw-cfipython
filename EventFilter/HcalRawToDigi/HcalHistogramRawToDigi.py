import FWCore.ParameterSet.Config as cms

def HcalHistogramRawToDigi(**kwargs):
  mod = cms.EDProducer('HcalHistogramRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
