import FWCore.ParameterSet.Config as cms

def CTPPSRandomDQMSource(**kwargs):
  mod = cms.EDProducer('CTPPSRandomDQMSource',
    tagRPixDigi = cms.InputTag('ctppsPixelDigisAlCaRecoProducer'),
    folderName = cms.untracked.string('PPSRANDOM/RandomPixel'),
    RPStatusWord = cms.untracked.uint32(32776),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
