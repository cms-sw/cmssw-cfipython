import FWCore.ParameterSet.Config as cms

def HLT2jetGapFilter(*args, **kwargs):
  mod = cms.EDFilter('HLT2jetGapFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('iterativeCone5CaloJets'),
    minEt = cms.double(90),
    minEta = cms.double(1.9),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
