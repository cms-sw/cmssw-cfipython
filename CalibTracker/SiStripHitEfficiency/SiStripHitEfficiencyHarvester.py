import FWCore.ParameterSet.Config as cms

def SiStripHitEfficiencyHarvester(*args, **kwargs):
  mod = cms.EDProducer('SiStripHitEfficiencyHarvester',
    inputFolder = cms.string('AlCaReco/SiStripHitEfficiency'),
    isAtPCL = cms.bool(False),
    doStoreOnDB = cms.bool(False),
    Record = cms.string('SiStripBadStrip'),
    Threshold = cms.double(0.1),
    Title = cms.string('Hit Efficiency'),
    nModsMin = cms.int32(5),
    doStoreOnTree = cms.untracked.bool(False),
    AutoIneffModTagging = cms.untracked.bool(False),
    TkMapMin = cms.untracked.double(0.9),
    EffPlotMin = cms.untracked.double(0.9),
    ShowRings = cms.untracked.bool(False),
    ShowEndcapSides = cms.untracked.bool(True),
    ShowTOB6TEC9 = cms.untracked.bool(False),
    ShowOnlyGoodModules = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
