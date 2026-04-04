import FWCore.ParameterSet.Config as cms

def HLTP2GTTauFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTP2GTTauFilter',
    saveTags = cms.bool(True),
    l1GTAlgoBlockTag = cms.InputTag(''),
    l1GTAlgoNames = cms.vstring(),
    minPt = cms.double(24),
    minN = cms.uint32(1),
    maxAbsEta = cms.double(1e+99),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
