import FWCore.ParameterSet.Config as cms

def HLTRapGapFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTRapGapFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('iterativeCone5CaloJets'),
    minEta = cms.double(3),
    maxEta = cms.double(5),
    caloThresh = cms.double(20),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
