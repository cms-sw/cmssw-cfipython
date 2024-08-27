import FWCore.ParameterSet.Config as cms

def HLTFEDSizeFilter(**kwargs):
  mod = cms.EDFilter('HLTFEDSizeFilter',
    saveTags = cms.bool(True),
    rawData = cms.InputTag('source'),
    threshold = cms.uint32(0),
    firstFED = cms.uint32(0),
    lastFED = cms.uint32(39),
    requireAllFEDs = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
