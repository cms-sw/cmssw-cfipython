import FWCore.ParameterSet.Config as cms

def HLT2jetGapFilter(**kwargs):
  mod = cms.EDFilter('HLT2jetGapFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('iterativeCone5CaloJets'),
    minEt = cms.double(90),
    minEta = cms.double(1.9),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
