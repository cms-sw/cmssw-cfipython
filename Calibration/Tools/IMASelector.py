import FWCore.ParameterSet.Config as cms

def IMASelector(*args, **kwargs):
  mod = cms.EDFilter('IMASelector',
    src = cms.InputTag(''),
    ESCOPinMin = cms.double(0),
    ESeedOPoutMin = cms.double(0),
    PinMPoutOPinMin = cms.double(0),
    ESCOPinMax = cms.double(0),
    ESeedOPoutMax = cms.double(0),
    PinMPoutOPinMax = cms.double(0),
    EMPoutMin = cms.double(0),
    EMPoutMax = cms.double(0),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
