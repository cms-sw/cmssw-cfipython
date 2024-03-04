import FWCore.ParameterSet.Config as cms

def SiStripMeanCMExtractor(**kwargs):
  mod = cms.EDProducer('SiStripMeanCMExtractor',
    CMCollection = cms.InputTag('siStripZeroSuppression', 'APVCM'),
    Algorithm = cms.string('Pedestals'),
    NEvents = cms.uint32(100),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
