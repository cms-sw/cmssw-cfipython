import FWCore.ParameterSet.Config as cms

def CSCChamberMasker(*args, **kwargs):
  mod = cms.EDProducer('CSCChamberMasker',
    stripDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCStripDigi'),
    wireDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCWireDigi'),
    comparatorDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCComparatorDigi'),
    rpcDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCRPCDigi'),
    alctDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCALCTDigi'),
    clctDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCCLCTDigi'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
