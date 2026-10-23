import FWCore.ParameterSet.Config as cms

def SiStripMeanCMExtractor(*args, **kwargs):
  mod = cms.EDProducer('SiStripMeanCMExtractor',
    CMCollection = cms.InputTag('siStripZeroSuppression', 'APVCM'),
    Algorithm = cms.string('Pedestals'),
    NEvents = cms.uint32(100),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
