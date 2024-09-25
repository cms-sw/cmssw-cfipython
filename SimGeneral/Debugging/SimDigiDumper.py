import FWCore.ParameterSet.Config as cms

def SimDigiDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('SimDigiDumper',
    ECalEBSrc = cms.InputTag('simEcalDigis', 'ebDigis'),
    ECalEESrc = cms.InputTag('simEcalDigis', 'eeDigis'),
    ECalESSrc = cms.InputTag('simEcalPreshowerDigis'),
    HCalSrc = cms.InputTag('simHcalDigis'),
    ZdcSrc = cms.InputTag('simHcalUnsuppressedDigis'),
    SiStripSrc = cms.InputTag('simSiStripDigis', 'ZeroSuppressed'),
    SiPxlSrc = cms.InputTag('simSiPixelDigis'),
    MuDTSrc = cms.InputTag('simMuonDTDigis'),
    MuCSCStripSrc = cms.InputTag('simMuonCSCDigis', 'MuonCSCStripDigi'),
    MuCSCWireSrc = cms.InputTag('simMuonCSCDigis', 'MuonCSCWireDigi'),
    MuRPCSrc = cms.InputTag('simMuonRPCDigis'),
    BTLSrc = cms.InputTag('mix', 'FTLBarrel'),
    ETLSrc = cms.InputTag('mix', 'FTLEndcap'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
