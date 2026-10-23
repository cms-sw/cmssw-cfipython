import FWCore.ParameterSet.Config as cms

def ScitagConfig(*args, **kwargs):
  mod = cms.Service('ScitagConfig',
    analysis = cms.untracked.PSet(
      primarySciTag = cms.untracked.uint32(206),
      embeddedSciTag = cms.untracked.uint32(215),
      preMixedPileupSciTag = cms.untracked.uint32(216)
    ),
    production = cms.untracked.PSet(
      primarySciTag = cms.untracked.uint32(204),
      embeddedSciTag = cms.untracked.uint32(215),
      preMixedPileupSciTag = cms.untracked.uint32(216)
    ),
    enable = cms.untracked.bool(True),
    productionCase = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
