import FWCore.ParameterSet.Config as cms

def HBHEstuckADCfilter(*args, **kwargs):
  mod = cms.EDFilter('HBHEstuckADCfilter',
    digiLabel = cms.InputTag('hcalDigis'),
    thresholdADC = cms.int32(100),
    writeList = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
