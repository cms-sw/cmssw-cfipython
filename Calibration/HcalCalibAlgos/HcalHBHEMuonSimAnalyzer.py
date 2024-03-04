import FWCore.ParameterSet.Config as cms

def HcalHBHEMuonSimAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalHBHEMuonSimAnalyzer',
    ModuleLabel = cms.string('g4SimHits'),
    EBCollection = cms.string('EcalHitsEB'),
    EECollection = cms.string('EcalHitsEE'),
    HCCollection = cms.string('HcalHits'),
    Verbosity = cms.untracked.int32(0),
    MaxDepth = cms.untracked.int32(7),
    EtaMax = cms.untracked.double(3),
    TimeMinCutECAL = cms.untracked.double(-500),
    TimeMaxCutECAL = cms.untracked.double(500),
    TimeMinCutHCAL = cms.untracked.double(-500),
    TimeMaxCutHCAL = cms.untracked.double(500),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
