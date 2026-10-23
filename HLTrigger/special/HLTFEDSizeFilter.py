import FWCore.ParameterSet.Config as cms

def HLTFEDSizeFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTFEDSizeFilter',
    saveTags = cms.bool(True),
    rawData = cms.InputTag('source'),
    threshold = cms.uint32(0),
    firstFED = cms.uint32(0),
    lastFED = cms.uint32(39),
    requireAllFEDs = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
