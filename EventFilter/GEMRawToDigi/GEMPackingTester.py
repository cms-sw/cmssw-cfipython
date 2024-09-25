import FWCore.ParameterSet.Config as cms

def GEMPackingTester(*args, **kwargs):
  mod = cms.EDAnalyzer('GEMPackingTester',
    fed = cms.InputTag('rawDataCollector'),
    gemDigi = cms.InputTag('muonGEMDigis'),
    gemSimDigi = cms.InputTag('simMuonGEMDigis'),
    readMultiBX = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
