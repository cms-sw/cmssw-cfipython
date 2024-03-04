import FWCore.ParameterSet.Config as cms

def CSCChamberMasker(**kwargs):
  mod = cms.EDProducer('CSCChamberMasker',
    stripDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCStripDigi'),
    wireDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCWireDigi'),
    comparatorDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCComparatorDigi'),
    rpcDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCRPCDigi'),
    alctDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCALCTDigi'),
    clctDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCCLCTDigi'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
