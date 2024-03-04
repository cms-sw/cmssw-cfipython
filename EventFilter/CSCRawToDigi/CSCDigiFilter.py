import FWCore.ParameterSet.Config as cms

def CSCDigiFilter(**kwargs):
  mod = cms.EDProducer('CSCDigiFilter',
    stripDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCStripDigi'),
    wireDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCWireDigi'),
    compDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCComparatorDigi'),
    alctDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCALCTDigi'),
    clctDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCCLCTDigi'),
    lctDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCCorrelatedLCTDigi'),
    showerDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCShowerDigi'),
    gemPadClusterDigiTag = cms.InputTag('muonCSCDigis', 'MuonGEMPadDigiCluster'),
    maskedChambers = cms.required.vstring,
    selectedChambers = cms.required.vstring,
    useGEMs = cms.bool(False),
    useShowers = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
