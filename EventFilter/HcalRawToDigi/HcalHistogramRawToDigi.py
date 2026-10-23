import FWCore.ParameterSet.Config as cms

def HcalHistogramRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('HcalHistogramRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
