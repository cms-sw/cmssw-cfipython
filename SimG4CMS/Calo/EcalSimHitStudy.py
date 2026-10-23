import FWCore.ParameterSet.Config as cms

def EcalSimHitStudy(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalSimHitStudy',
    ModuleLabel = cms.untracked.string('g4SimHits'),
    CaloCollection = cms.untracked.vstring(),
    SourceLabel = cms.untracked.string('VtxSmeared'),
    MaxEnergy = cms.untracked.double(200),
    TimeCut = cms.untracked.double(100),
    SelectX = cms.untracked.int32(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
