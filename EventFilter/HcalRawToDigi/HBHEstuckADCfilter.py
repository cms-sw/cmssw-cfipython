import FWCore.ParameterSet.Config as cms

def HBHEstuckADCfilter(**kwargs):
  mod = cms.EDFilter('HBHEstuckADCfilter',
    digiLabel = cms.InputTag('hcalDigis'),
    thresholdADC = cms.int32(100),
    writeList = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
