import FWCore.ParameterSet.Config as cms

def ScitagConfig(*args, **kwargs):
  mod = cms.Service('ScitagConfig',
    analysis = cms.untracked.PSet(
      primarySciTag = cms.untracked.uint32(196664),
      embeddedSciTag = cms.untracked.uint32(196700),
      preMixedPileupSciTag = cms.untracked.uint32(196704)
    ),
    production = cms.untracked.PSet(
      primarySciTag = cms.untracked.uint32(196656),
      embeddedSciTag = cms.untracked.uint32(196700),
      preMixedPileupSciTag = cms.untracked.uint32(196704)
    ),
    enable = cms.untracked.bool(True),
    productionCase = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
