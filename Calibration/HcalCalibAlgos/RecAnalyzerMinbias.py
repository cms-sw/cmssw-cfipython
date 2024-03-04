import FWCore.ParameterSet.Config as cms

def RecAnalyzerMinbias(**kwargs):
  mod = cms.EDAnalyzer('RecAnalyzerMinbias',
    runNZS = cms.bool(True),
    noise = cms.bool(False),
    eLowHB = cms.double(4),
    eHighHB = cms.double(100),
    eLowHE = cms.double(4),
    eHighHE = cms.double(150),
    eLowHF = cms.double(10),
    eHighHF = cms.double(150),
    eMin = cms.untracked.double(2),
    runMin = cms.untracked.int32(308327),
    runMax = cms.untracked.int32(308347),
    triggerBits = cms.untracked.vint32(),
    ignoreL1 = cms.untracked.bool(False),
    corrFile = cms.untracked.string('CorFactor.txt'),
    fillHisto = cms.untracked.bool(False),
    extraHisto = cms.untracked.bool(False),
    hcalIeta = cms.untracked.vint32(),
    hcalIphi = cms.untracked.vint32(),
    hcalDepth = cms.untracked.vint32(),
    hbheInputMB = cms.InputTag('hbherecoMB'),
    hfInputMB = cms.InputTag('hfrecoMB'),
    gtDigisAlCaMB = cms.InputTag('gtDigisAlCaMB'),
    hcalDigiCollectionTag = cms.InputTag('hcalDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
