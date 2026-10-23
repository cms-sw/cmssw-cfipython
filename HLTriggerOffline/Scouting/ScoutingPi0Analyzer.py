import FWCore.ParameterSet.Config as cms

def ScoutingPi0Analyzer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingPi0Analyzer',
    scoutingCollection = cms.InputTag('hltScoutingPFPacker'),
    OutputInternalPath = cms.string('HLT/ScoutingOffline/PiZero'),
    minPt = cms.double(1.5),
    maxEta = cms.double(2.5),
    isolationCone = cms.double(0.2),
    isolationPtRatio = cms.double(0.8),
    pairMaxDr = cms.double(0.1),
    asymmetryCut = cms.double(0.85),
    pairMinPt = cms.double(2),
    maxMass = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
