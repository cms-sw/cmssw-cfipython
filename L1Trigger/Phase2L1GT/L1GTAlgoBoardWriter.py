import FWCore.ParameterSet.Config as cms

def L1GTAlgoBoardWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('L1GTAlgoBoardWriter',
    filename = cms.required.untracked.string,
    fileExtension = cms.untracked.string('txt'),
    algoBlocksTag = cms.required.untracked.InputTag,
    maxEvents = cms.untracked.uint32(0),
    channels = cms.required.untracked.vuint32,
    algoBitMask = cms.untracked.vuint64(
      18446744073709551615,
      18446744073709551615,
      18446744073709551615,
      18446744073709551615,
      18446744073709551615,
      18446744073709551615,
      18446744073709551615,
      18446744073709551615,
      18446744073709551615
    ),
    maxFrames = cms.untracked.uint32(1024),
    patternFormat = cms.untracked.string('EMPv2'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
