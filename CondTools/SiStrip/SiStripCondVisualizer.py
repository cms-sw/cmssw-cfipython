import FWCore.ParameterSet.Config as cms

def SiStripCondVisualizer(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripCondVisualizer',
    doNoise = cms.bool(False),
    doPeds = cms.bool(False),
    doG1 = cms.bool(False),
    doG2 = cms.bool(False),
    doBadComps = cms.bool(False),
    StripQualityLabel = cms.string('MergedBadComponent'),
    selections = cms.VPSet(
      cms.PSet(
        detLabel = cms.string('Tracker'),
        detSelection = cms.uint32(1),
        selection = cms.untracked.vstring(
          '0x1e000000-0x16000000',
          '0x1e006000-0x18002000',
          '0x1e006000-0x18004000',
          '0x1e000000-0x1a000000',
          '0x1e0c0000-0x1c040000',
          '0x1e0c0000-0x1c080000'
        )
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
