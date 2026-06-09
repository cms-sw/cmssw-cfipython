import FWCore.ParameterSet.Config as cms

def CTPPSRandomDQMSource(*args, **kwargs):
  mod = cms.EDProducer('CTPPSRandomDQMSource',
    tagRPixDigi = cms.InputTag('ctppsPixelDigisAlCaRecoProducer'),
    folderName = cms.untracked.string('PPSRANDOM/RandomPixel'),
    RPStatusWord = cms.untracked.uint32(32776),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
