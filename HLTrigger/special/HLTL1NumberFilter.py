import FWCore.ParameterSet.Config as cms

def HLTL1NumberFilter(**kwargs):
  mod = cms.EDFilter('HLTL1NumberFilter',
    rawInput = cms.InputTag('source'),
    period = cms.uint32(4096),
    invert = cms.bool(True),
    fedId = cms.int32(812),
    useTCDSEventNumber = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
