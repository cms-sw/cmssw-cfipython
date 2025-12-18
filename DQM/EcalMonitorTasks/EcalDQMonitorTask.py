import FWCore.ParameterSet.Config as cms

def EcalDQMonitorTask(*args, **kwargs):
  mod = cms.EDProducer('EcalDQMonitorTask',
    moduleName = cms.untracked.string('Ecal Monitor Module'),
    workers = cms.required.untracked.vstring,
    verbosity = cms.untracked.int32(0),
    commonParameters = cms.untracked.PSet(
      onlineMode = cms.untracked.bool(False),
      willConvertToEDM = cms.untracked.bool(True)
    ),
    workerParameters = cms.untracked.PSet(
      allowAnyLabel_ = cms.required.untracked.PSetTemplate(
        onlineMode = cms.untracked.bool(False),
        willConvertToEDM = cms.untracked.bool(True),
        MEs = cms.untracked.PSet(
          allowAnyLabel_ = cms.required.untracked.PSetTemplate(
            path = cms.required.untracked.string,
            kind = cms.required.untracked.string,
            otype = cms.required.untracked.string,
            btype = cms.required.untracked.string,
            description = cms.required.untracked.string,
            online = cms.untracked.bool(False),
            perLumi = cms.untracked.bool(False),
            minutely = cms.optional.untracked.bool,
            cumulative = cms.optional.untracked.bool,
            shiftAxis = cms.optional.untracked.bool,
            xaxis = cms.untracked.PSet(
              title = cms.untracked.string(''),
              nbins = cms.untracked.int32(0),
              low = cms.untracked.double(0),
              edges = cms.optional.untracked.vdouble,
              labels = cms.optional.untracked.vstring
            ),
            yaxis = cms.untracked.PSet(
              title = cms.untracked.string(''),
              nbins = cms.untracked.int32(0),
              low = cms.untracked.double(0),
              edges = cms.optional.untracked.vdouble,
              labels = cms.optional.untracked.vstring
            ),
            zaxis = cms.untracked.PSet(
              title = cms.untracked.string(''),
              nbins = cms.untracked.int32(0),
              low = cms.untracked.double(0),
              edges = cms.optional.untracked.vdouble,
              labels = cms.optional.untracked.vstring
            ),
            multi = cms.untracked.PSet(
              allowAnyLabel_ = cms.optional.untracked.vstring
            )
          )
        ),
        params = cms.untracked.PSet()
      )
    ),
    collectionTags = cms.PSet(
      allowAnyLabel_ = cms.optional.untracked.InputTag
    ),
    skipCollections = cms.untracked.vstring(),
    allowMissingCollections = cms.untracked.bool(True),
    resetInterval = cms.untracked.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
