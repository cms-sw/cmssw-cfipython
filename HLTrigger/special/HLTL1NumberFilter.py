import FWCore.ParameterSet.Config as cms

def HLTL1NumberFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTL1NumberFilter',
    rawInput = cms.InputTag('source'),
    period = cms.uint32(4096),
    invert = cms.bool(True),
    fedId = cms.int32(812),
    useTCDSEventNumber = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
