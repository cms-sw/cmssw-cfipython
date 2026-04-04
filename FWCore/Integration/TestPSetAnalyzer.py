import FWCore.ParameterSet.Config as cms

def TestPSetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestPSetAnalyzer',
    testLumi = cms.required.LuminosityBlockID,
    testVLumi = cms.required.VLuminosityBlockID,
    testRange = cms.required.LuminosityBlockRange,
    testVRange = cms.required.VLuminosityBlockRange,
    testERange = cms.required.EventRange,
    testVERange = cms.required.VEventRange,
    testEventID1 = cms.required.EventID,
    testEventID2 = cms.required.EventID,
    testEventID3 = cms.required.EventID,
    testEventID4 = cms.required.EventID,
    testVEventID = cms.required.VEventID,
    testERange1 = cms.required.EventRange,
    testERange2 = cms.required.EventRange,
    testERange3 = cms.required.EventRange,
    testERange4 = cms.required.EventRange,
    testERange5 = cms.required.EventRange,
    testVERange2 = cms.required.VEventRange,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
