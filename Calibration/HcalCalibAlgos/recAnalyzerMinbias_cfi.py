import FWCore.ParameterSet.Config as cms

recAnalyzerMinbias = cms.EDAnalyzer('RecAnalyzerMinbias',
  runNZS = cms.bool(True),
  noise = cms.bool(False),
  eLowHB = cms.double(4),
  eHighHB = cms.double(100),
  eLowHE = cms.double(4),
  eHighHE = cms.double(150),
  eLowHF = cms.double(10),
  eHighHF = cms.double(150),
  eMin = cms.untracked.double(2),
  runMin = cms.untracked.int32(303442),
  runMax = cms.untracked.int32(304825),
  triggerBits = cms.untracked.vint32(),
  ignoreL1 = cms.untracked.bool(False),
  corrFile = cms.untracked.string('CorFactor.txt'),
  fillHisto = cms.untracked.bool(False),
  hcalIeta = cms.untracked.vint32(),
  hcalIphi = cms.untracked.vint32(),
  hcalDepth = cms.untracked.vint32(),
  hbheInputMB = cms.InputTag('hbherecoMB'),
  hfInputMB = cms.InputTag('hfrecoMB')
)
