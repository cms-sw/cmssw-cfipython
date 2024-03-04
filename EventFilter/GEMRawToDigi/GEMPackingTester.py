import FWCore.ParameterSet.Config as cms

def GEMPackingTester(**kwargs):
  mod = cms.EDAnalyzer('GEMPackingTester',
    fed = cms.InputTag('rawDataCollector'),
    gemDigi = cms.InputTag('muonGEMDigis'),
    gemSimDigi = cms.InputTag('simMuonGEMDigis'),
    readMultiBX = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
