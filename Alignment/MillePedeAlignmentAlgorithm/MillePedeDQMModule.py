import FWCore.ParameterSet.Config as cms

def MillePedeDQMModule(*args, **kwargs):
  mod = cms.EDProducer('MillePedeDQMModule',
    outputFolder = cms.string('AlCaReco/SiPixelAli'),
    MillePedeFileReader = cms.PSet(
      fileDir = cms.string(''),
      ignoreInactiveAlignables = cms.bool(True),
      millePedeEndFile = cms.string('millepede.end'),
      millePedeLogFile = cms.string('millepede.log'),
      millePedeResFile = cms.string('millepede.res'),
      isHG = cms.bool(False)
    ),
    alignmentTokenSrc = cms.InputTag('SiPixelAliPedeAlignmentProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
